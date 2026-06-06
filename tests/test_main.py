import pytest
import main

def test_k8scostoptimizer_instantiation():
    # Verify that the class K8sCostOptimizer is inspectable and loadable
    assert hasattr(main, 'K8sCostOptimizer')

