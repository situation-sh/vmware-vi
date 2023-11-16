# OperationDisallowedOnHost

An OperationDisallowedOnHost is thrown if an operation is diasllowed on host when a direct connection is used.  Examples for such operations include VM powering on / memory hot-plug which could potentially violate hard-enforcement licenses if allowed on host. The functionality these operations provide is still available, but only through calls to an external entity.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.operation_disallowed_on_host import OperationDisallowedOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDisallowedOnHost from a JSON string
operation_disallowed_on_host_instance = OperationDisallowedOnHost.from_json(json)
# print the JSON string representation of the object
print OperationDisallowedOnHost.to_json()

# convert the object into a dict
operation_disallowed_on_host_dict = operation_disallowed_on_host_instance.to_dict()
# create an instance of OperationDisallowedOnHost from a dict
operation_disallowed_on_host_form_dict = operation_disallowed_on_host.from_dict(operation_disallowed_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


