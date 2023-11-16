# RetrieveHostCustomizationsRequestType

The parameters of *HostProfileManager.RetrieveHostCustomizations*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts with which the answer files are associated.  ***Required privileges:*** Profile.Edit  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_host_customizations_request_type import RetrieveHostCustomizationsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveHostCustomizationsRequestType from a JSON string
retrieve_host_customizations_request_type_instance = RetrieveHostCustomizationsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveHostCustomizationsRequestType.to_json()

# convert the object into a dict
retrieve_host_customizations_request_type_dict = retrieve_host_customizations_request_type_instance.to_dict()
# create an instance of RetrieveHostCustomizationsRequestType from a dict
retrieve_host_customizations_request_type_form_dict = retrieve_host_customizations_request_type.from_dict(retrieve_host_customizations_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


