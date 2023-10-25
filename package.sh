#!/bin/bash

rm competition.zip

zip -j scoring_program.zip ./scoring_program/*

zip -j warmup_ground_truth.zip ./warmup/ground_truth.json

zip -j public_ground_truth.zip ./public/ground_truth.json

zip -j private_ground_truth.zip ./private/ground_truth.json

zip competition.zip competition.yaml data.html evaluation.html logo.png overview.html terms.html scoring_program.zip warmup_ground_truth.zip public_ground_truth.zip private_ground_truth.zip

rm warmup_ground_truth.zip

rm public_ground_truth.zip

rm private_ground_truth.zip

rm scoring_program.zip