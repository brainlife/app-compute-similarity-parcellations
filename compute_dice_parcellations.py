#/usr/bin/env python3

import os, sys
import nibabel as nib
import numpy as np
import json
import pandas as pd

def dice_coefficient(compare_img,ref_img,k=1):

    # set up prediction and true data
    pred = compare_img
    true = ref_img

    # compute dice
    intersection = np.sum(pred[true==k]) * 2.0
    dice = intersection / (np.sum(pred) + np.sum(true))

    return dice

def create_binary_label(img,label):

    # grab data from img to make roi
    roi = img.get_fdata()

    # identify voxels where the data is equal to the label, and then compute inverse
    index = roi == label
    inverse_index = np.invert(index)

    # set values where data equal index to 1, all else zero and return
    roi[index] = 1
    roi[inverse_index] = 0

    return roi

def main():

    # load configuration json
    with open('config.json','r') as config_f:
        config = json.load(config_f)

    # grab label.json
    with open(config['labels'],'r') as labels_f:
        labels_json = json.load(labels_f)

    # grab subject and session id
    subject_id = config['_inputs'][0]['meta']['subject']

    # set paths to parcellations
    compare_path = config['parc_compare']
    ref_path = config['parc_reference']

    # identify unique labels
    ref = nib.load(ref_path)
    unique_labels = np.unique(ref.get_fdata().flatten())[1:]

    # grab parcellation names and labels
    structure_id = [ f["name"] for f in labels_json if int(f["label"]) in unique_labels]

    # compute dice coefficient by looping through individual labels
    dice = []; node_id = []

    for i in range(len(unique_labels)):

        # load data
        compare = nib.load(compare_path)
        ref = nib.load(ref_path)

        ref_roi = create_binary_label(ref,unique_labels[i])
        compare_roi = create_binary_label(compare,unique_labels[i])

        dice = np.append(dice,dice_coefficient(compare_roi,ref_roi,1))
        node_id = np.append(node_id,unique_labels[i])

    # create pandas dataframe
    output_df = pd.DataFrame()
    output_df['subjectID'] = [ subject_id for f in range(len(dice)) ]
    output_df['structureID'] = structure_id
    output_df['nodeID'] = unique_labels
    if not output_df.nodeID.dtype == 'O':
        if output_df.nodeID.dtype == 'float64' or output_df.nodeID.dtype == 'int64':
            output_df['nodeID'] = output_df.nodeID.astype(int).astype(str)
        else:
            output_df['nodeID'] = output_df.nodeID.astype(str)
    output_df['dice'] = dice

    # create output directory if not already there
    if not os.path.isdir('./parc_stats'):
        os.mkdir('./parc_stats')
    if not os.path.isdir('./parc_stats/parc-stats'):
        os.mkdir('./parc_stats/parc-stats')

    # save output_df to output directory
    output_df.to_csv('./parc_stats/parc-stats/parcellation.csv',index=False)

if __name__ == '__main__':
    main()
