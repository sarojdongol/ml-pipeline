#!/usr/bin/env python3

from aws_cdk import core

from ml_pipeline.ml_pipeline_stack import MlPipelineStack


app = core.App()
MlPipelineStack(app, "ml-pipeline")

app.synth()
