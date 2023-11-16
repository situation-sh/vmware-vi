# RetrieveHostSpecificationRequestType

The parameters of *HostSpecificationManager.RetrieveHostSpecification*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**from_host** | **bool** | Whether retrieve from the host.  | 

## Example

```python
from vmware_vi.models.retrieve_host_specification_request_type import RetrieveHostSpecificationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveHostSpecificationRequestType from a JSON string
retrieve_host_specification_request_type_instance = RetrieveHostSpecificationRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveHostSpecificationRequestType.to_json()

# convert the object into a dict
retrieve_host_specification_request_type_dict = retrieve_host_specification_request_type_instance.to_dict()
# create an instance of RetrieveHostSpecificationRequestType from a dict
retrieve_host_specification_request_type_form_dict = retrieve_host_specification_request_type.from_dict(retrieve_host_specification_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


