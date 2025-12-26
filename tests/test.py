import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from lab7 import centroid

@pytest.fixture
def get_arrays():
    test_x = np.float64(np.loadtxt("tests/test_x.csv",delimiter=","))
    test_y = np.float64(np.loadtxt("tests/test_y.csv",delimiter=","))
    test_m = np.float64(np.loadtxt("tests/test_m.csv",delimiter=","))
    test_out = np.float64(np.loadtxt("tests/test_out.csv",delimiter=","))
    return test_x, test_y, test_m, test_out

def test_cx(get_arrays):
    test_data = get_arrays
    
    test_x = test_data[0]
    test_y = test_data[1]
    test_m = test_data[2]
    test_out = test_data[3]
    
    for i in range(len(test_x)):
        res = centroid(test_x[i,0],
                      test_y[i,0],
                      test_x[i,1],
                      test_y[i,1],
                      test_x[i,2],
                      test_y[i,2],
                      test_m[i,0],
                      test_m[i,1],
                      test_m[i,2])
                      
        assert test_out[i,0] == res[0]

def test_cy(get_arrays):
    test_data = get_arrays
    
    test_x = test_data[0]
    test_y = test_data[1]
    test_m = test_data[2]
    test_out = test_data[3]
    
    for i in range(len(test_x)):
        res = centroid(test_x[i,0],
                      test_y[i,0],
                      test_x[i,1],
                      test_y[i,1],
                      test_x[i,2],
                      test_y[i,2],
                      test_m[i,0],
                      test_m[i,1],
                      test_m[i,2])
                      
        assert test_out[i,1] == res[1]

def test_totalm(get_arrays):
    test_data = get_arrays
    
    test_x = test_data[0]
    test_y = test_data[1]
    test_m = test_data[2]
    test_out = test_data[3]
    
    for i in range(len(test_x)):
        res = centroid(test_x[i,0],
                      test_y[i,0],
                      test_x[i,1],
                      test_y[i,1],
                      test_x[i,2],
                      test_y[i,2],
                      test_m[i,0],
                      test_m[i,1],
                      test_m[i,2])
                      
        assert test_out[i,2] == res[2]
        
