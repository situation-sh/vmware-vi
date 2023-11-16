# HostSpecificationOperationFailed

Fault thrown when an operation, on host specification or host sub specification for a host, failed.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_specification_operation_failed import HostSpecificationOperationFailed

# TODO update the JSON string below
json = "{}"
# create an instance of HostSpecificationOperationFailed from a JSON string
host_specification_operation_failed_instance = HostSpecificationOperationFailed.from_json(json)
# print the JSON string representation of the object
print HostSpecificationOperationFailed.to_json()

# convert the object into a dict
host_specification_operation_failed_dict = host_specification_operation_failed_instance.to_dict()
# create an instance of HostSpecificationOperationFailed from a dict
host_specification_operation_failed_form_dict = host_specification_operation_failed.from_dict(host_specification_operation_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


