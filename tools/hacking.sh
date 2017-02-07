#!/bin/bash
flake8 cloudeyeclient | tee flake8.log
exit ${PIPESTATUS[0]}
