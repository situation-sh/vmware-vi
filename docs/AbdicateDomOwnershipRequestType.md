# AbdicateDomOwnershipRequestType

The parameters of *HostVsanInternalSystem.AbdicateDomOwnership*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of VSAN/DOM object UUIDs.  | 

## Example

```python
from vmware_vi.models.abdicate_dom_ownership_request_type import AbdicateDomOwnershipRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AbdicateDomOwnershipRequestType from a JSON string
abdicate_dom_ownership_request_type_instance = AbdicateDomOwnershipRequestType.from_json(json)
# print the JSON string representation of the object
print AbdicateDomOwnershipRequestType.to_json()

# convert the object into a dict
abdicate_dom_ownership_request_type_dict = abdicate_dom_ownership_request_type_instance.to_dict()
# create an instance of AbdicateDomOwnershipRequestType from a dict
abdicate_dom_ownership_request_type_form_dict = abdicate_dom_ownership_request_type.from_dict(abdicate_dom_ownership_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


