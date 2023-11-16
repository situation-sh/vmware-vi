# FaultToleranceNotSameBuild

The destination host does not have the same build or Fault Tolerance feature version number as the source host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **str** | The string.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.fault_tolerance_not_same_build import FaultToleranceNotSameBuild

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceNotSameBuild from a JSON string
fault_tolerance_not_same_build_instance = FaultToleranceNotSameBuild.from_json(json)
# print the JSON string representation of the object
print FaultToleranceNotSameBuild.to_json()

# convert the object into a dict
fault_tolerance_not_same_build_dict = fault_tolerance_not_same_build_instance.to_dict()
# create an instance of FaultToleranceNotSameBuild from a dict
fault_tolerance_not_same_build_form_dict = fault_tolerance_not_same_build.from_dict(fault_tolerance_not_same_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


