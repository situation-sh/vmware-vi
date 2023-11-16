# DeviceGroupId

Identifier of a replication device group.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the device group.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.device_group_id import DeviceGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupId from a JSON string
device_group_id_instance = DeviceGroupId.from_json(json)
# print the JSON string representation of the object
print DeviceGroupId.to_json()

# convert the object into a dict
device_group_id_dict = device_group_id_instance.to_dict()
# create an instance of DeviceGroupId from a dict
device_group_id_form_dict = device_group_id.from_dict(device_group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


