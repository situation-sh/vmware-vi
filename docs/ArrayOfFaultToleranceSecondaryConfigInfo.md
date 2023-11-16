# ArrayOfFaultToleranceSecondaryConfigInfo

A boxed array of *FaultToleranceSecondaryConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultToleranceSecondaryConfigInfo]**](FaultToleranceSecondaryConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fault_tolerance_secondary_config_info import ArrayOfFaultToleranceSecondaryConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultToleranceSecondaryConfigInfo from a JSON string
array_of_fault_tolerance_secondary_config_info_instance = ArrayOfFaultToleranceSecondaryConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultToleranceSecondaryConfigInfo.to_json()

# convert the object into a dict
array_of_fault_tolerance_secondary_config_info_dict = array_of_fault_tolerance_secondary_config_info_instance.to_dict()
# create an instance of ArrayOfFaultToleranceSecondaryConfigInfo from a dict
array_of_fault_tolerance_secondary_config_info_form_dict = array_of_fault_tolerance_secondary_config_info.from_dict(array_of_fault_tolerance_secondary_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


