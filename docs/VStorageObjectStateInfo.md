# VStorageObjectStateInfo

Contains information of a virtual storage object state.  NOTE: The information obtained with this object is dynamic and it could change during the lifetime of the object. For performance purposes some of the data may not reflect the immediate state of the object, also there is not guarantee that it will be provided.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tentative** | **bool** | If set this flag indicates that the object currently is part of provisioning operation or the last operation has not finished gracefully.  There are maintenance procedures that are working on resolving that tentative state. Note that this might result in the object to be removed.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.v_storage_object_state_info import VStorageObjectStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectStateInfo from a JSON string
v_storage_object_state_info_instance = VStorageObjectStateInfo.from_json(json)
# print the JSON string representation of the object
print VStorageObjectStateInfo.to_json()

# convert the object into a dict
v_storage_object_state_info_dict = v_storage_object_state_info_instance.to_dict()
# create an instance of VStorageObjectStateInfo from a dict
v_storage_object_state_info_form_dict = v_storage_object_state_info.from_dict(v_storage_object_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


