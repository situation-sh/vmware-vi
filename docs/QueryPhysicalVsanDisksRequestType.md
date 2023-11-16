# QueryPhysicalVsanDisksRequestType

The parameters of *HostVsanInternalSystem.QueryPhysicalVsanDisks*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**props** | **List[str]** | List of properties to gather. Not specifying a list will fetch all properties.  | [optional] 

## Example

```python
from vmware_vi.models.query_physical_vsan_disks_request_type import QueryPhysicalVsanDisksRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPhysicalVsanDisksRequestType from a JSON string
query_physical_vsan_disks_request_type_instance = QueryPhysicalVsanDisksRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPhysicalVsanDisksRequestType.to_json()

# convert the object into a dict
query_physical_vsan_disks_request_type_dict = query_physical_vsan_disks_request_type_instance.to_dict()
# create an instance of QueryPhysicalVsanDisksRequestType from a dict
query_physical_vsan_disks_request_type_form_dict = query_physical_vsan_disks_request_type.from_dict(query_physical_vsan_disks_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


