# DeleteVsanObjectsRequestType

The parameters of *HostVsanInternalSystem.DeleteVsanObjects*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of object UUIDs to be deleted.  | 
**force** | **bool** | Optional force delete.  | [optional] 

## Example

```python
from vmware_vi.models.delete_vsan_objects_request_type import DeleteVsanObjectsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVsanObjectsRequestType from a JSON string
delete_vsan_objects_request_type_instance = DeleteVsanObjectsRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteVsanObjectsRequestType.to_json()

# convert the object into a dict
delete_vsan_objects_request_type_dict = delete_vsan_objects_request_type_instance.to_dict()
# create an instance of DeleteVsanObjectsRequestType from a dict
delete_vsan_objects_request_type_form_dict = delete_vsan_objects_request_type.from_dict(delete_vsan_objects_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


