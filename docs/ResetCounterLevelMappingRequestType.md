# ResetCounterLevelMappingRequestType

The parameters of *PerformanceManager.ResetCounterLevelMapping*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | **List[int]** | An array of counter ids.  | 

## Example

```python
from vmware_vi.models.reset_counter_level_mapping_request_type import ResetCounterLevelMappingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResetCounterLevelMappingRequestType from a JSON string
reset_counter_level_mapping_request_type_instance = ResetCounterLevelMappingRequestType.from_json(json)
# print the JSON string representation of the object
print ResetCounterLevelMappingRequestType.to_json()

# convert the object into a dict
reset_counter_level_mapping_request_type_dict = reset_counter_level_mapping_request_type_instance.to_dict()
# create an instance of ResetCounterLevelMappingRequestType from a dict
reset_counter_level_mapping_request_type_form_dict = reset_counter_level_mapping_request_type.from_dict(reset_counter_level_mapping_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


