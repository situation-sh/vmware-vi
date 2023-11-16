# HostVsanInternalSystemCmmdsQuery

All fields in the CMMDS Query spec are optional, but at least one needs specified to make a valid query.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | CMMDS type, e.g.  DOM\\_OBJECT, LSOM\\_OBJECT, POLICY, DISK etc.  ***Since:*** vSphere API 5.5  | [optional] 
**uuid** | **str** | UUID of the entry.  ***Since:*** vSphere API 5.5  | [optional] 
**owner** | **str** | UUID of the owning node.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_vsan_internal_system_cmmds_query import HostVsanInternalSystemCmmdsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of HostVsanInternalSystemCmmdsQuery from a JSON string
host_vsan_internal_system_cmmds_query_instance = HostVsanInternalSystemCmmdsQuery.from_json(json)
# print the JSON string representation of the object
print HostVsanInternalSystemCmmdsQuery.to_json()

# convert the object into a dict
host_vsan_internal_system_cmmds_query_dict = host_vsan_internal_system_cmmds_query_instance.to_dict()
# create an instance of HostVsanInternalSystemCmmdsQuery from a dict
host_vsan_internal_system_cmmds_query_form_dict = host_vsan_internal_system_cmmds_query.from_dict(host_vsan_internal_system_cmmds_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


