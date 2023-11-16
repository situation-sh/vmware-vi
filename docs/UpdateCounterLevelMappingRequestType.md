# UpdateCounterLevelMappingRequestType

The parameters of *PerformanceManager.UpdateCounterLevelMapping*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_level_map** | [**List[PerformanceManagerCounterLevelMapping]**](PerformanceManagerCounterLevelMapping.md) | An array of *PerformanceManagerCounterLevelMapping* objects. The levels for the counters passed in are changed to the passed in values. If the optional aggregateLevel field is left unset then only the perDeviceLevel is configured. If the optional perDeviceLevel is left unset then only the aggregateLevel is configured. If there are multiple entries in the passed in array for the same counterId being updated then the last entry containing the counterId takes effect.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.update_counter_level_mapping_request_type import UpdateCounterLevelMappingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCounterLevelMappingRequestType from a JSON string
update_counter_level_mapping_request_type_instance = UpdateCounterLevelMappingRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateCounterLevelMappingRequestType.to_json()

# convert the object into a dict
update_counter_level_mapping_request_type_dict = update_counter_level_mapping_request_type_instance.to_dict()
# create an instance of UpdateCounterLevelMappingRequestType from a dict
update_counter_level_mapping_request_type_form_dict = update_counter_level_mapping_request_type.from_dict(update_counter_level_mapping_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


