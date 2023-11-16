# QueryCandidateNicsRequestType

The parameters of *IscsiManager.QueryCandidateNics*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_name** | **str** | iSCSI Adapter name for which the method to be applied.  | 

## Example

```python
from vmware_vi.models.query_candidate_nics_request_type import QueryCandidateNicsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCandidateNicsRequestType from a JSON string
query_candidate_nics_request_type_instance = QueryCandidateNicsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryCandidateNicsRequestType.to_json()

# convert the object into a dict
query_candidate_nics_request_type_dict = query_candidate_nics_request_type_instance.to_dict()
# create an instance of QueryCandidateNicsRequestType from a dict
query_candidate_nics_request_type_form_dict = query_candidate_nics_request_type.from_dict(query_candidate_nics_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


