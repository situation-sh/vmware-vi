# ArrayOfDestinationVsanDisabled

A boxed array of *DestinationVsanDisabled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DestinationVsanDisabled]**](DestinationVsanDisabled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_destination_vsan_disabled import ArrayOfDestinationVsanDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDestinationVsanDisabled from a JSON string
array_of_destination_vsan_disabled_instance = ArrayOfDestinationVsanDisabled.from_json(json)
# print the JSON string representation of the object
print ArrayOfDestinationVsanDisabled.to_json()

# convert the object into a dict
array_of_destination_vsan_disabled_dict = array_of_destination_vsan_disabled_instance.to_dict()
# create an instance of ArrayOfDestinationVsanDisabled from a dict
array_of_destination_vsan_disabled_form_dict = array_of_destination_vsan_disabled.from_dict(array_of_destination_vsan_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


