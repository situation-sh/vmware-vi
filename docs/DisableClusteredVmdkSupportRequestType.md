# DisableClusteredVmdkSupportRequestType

The parameters of *HostDatastoreSystem.DisableClusteredVmdkSupport*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.disable_clustered_vmdk_support_request_type import DisableClusteredVmdkSupportRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisableClusteredVmdkSupportRequestType from a JSON string
disable_clustered_vmdk_support_request_type_instance = DisableClusteredVmdkSupportRequestType.from_json(json)
# print the JSON string representation of the object
print DisableClusteredVmdkSupportRequestType.to_json()

# convert the object into a dict
disable_clustered_vmdk_support_request_type_dict = disable_clustered_vmdk_support_request_type_instance.to_dict()
# create an instance of DisableClusteredVmdkSupportRequestType from a dict
disable_clustered_vmdk_support_request_type_form_dict = disable_clustered_vmdk_support_request_type.from_dict(disable_clustered_vmdk_support_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


