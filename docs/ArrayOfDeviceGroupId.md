# ArrayOfDeviceGroupId

A boxed array of *DeviceGroupId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DeviceGroupId]**](DeviceGroupId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_device_group_id import ArrayOfDeviceGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDeviceGroupId from a JSON string
array_of_device_group_id_instance = ArrayOfDeviceGroupId.from_json(json)
# print the JSON string representation of the object
print ArrayOfDeviceGroupId.to_json()

# convert the object into a dict
array_of_device_group_id_dict = array_of_device_group_id_instance.to_dict()
# create an instance of ArrayOfDeviceGroupId from a dict
array_of_device_group_id_form_dict = array_of_device_group_id.from_dict(array_of_device_group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


