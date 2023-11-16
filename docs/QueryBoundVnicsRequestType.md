# QueryBoundVnicsRequestType

The parameters of *IscsiManager.QueryBoundVnics*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_name** | **str** | iSCSI adapter name for which the method to be applied.  | 

## Example

```python
from vmware_vi.models.query_bound_vnics_request_type import QueryBoundVnicsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBoundVnicsRequestType from a JSON string
query_bound_vnics_request_type_instance = QueryBoundVnicsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryBoundVnicsRequestType.to_json()

# convert the object into a dict
query_bound_vnics_request_type_dict = query_bound_vnics_request_type_instance.to_dict()
# create an instance of QueryBoundVnicsRequestType from a dict
query_bound_vnics_request_type_form_dict = query_bound_vnics_request_type.from_dict(query_bound_vnics_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


