# QueryDisksForVsanRequestType

The parameters of *HostVsanSystem.QueryDisksForVsan*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_name** | **List[str]** | may be set to restrict the query to the list of *HostScsiDisk* objects named by the given paths  | [optional] 

## Example

```python
from vmware_vi.models.query_disks_for_vsan_request_type import QueryDisksForVsanRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDisksForVsanRequestType from a JSON string
query_disks_for_vsan_request_type_instance = QueryDisksForVsanRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDisksForVsanRequestType.to_json()

# convert the object into a dict
query_disks_for_vsan_request_type_dict = query_disks_for_vsan_request_type_instance.to_dict()
# create an instance of QueryDisksForVsanRequestType from a dict
query_disks_for_vsan_request_type_form_dict = query_disks_for_vsan_request_type.from_dict(query_disks_for_vsan_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


