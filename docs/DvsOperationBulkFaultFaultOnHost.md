# DvsOperationBulkFaultFaultOnHost

The fault occurred on the host during an operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.dvs_operation_bulk_fault_fault_on_host import DvsOperationBulkFaultFaultOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of DvsOperationBulkFaultFaultOnHost from a JSON string
dvs_operation_bulk_fault_fault_on_host_instance = DvsOperationBulkFaultFaultOnHost.from_json(json)
# print the JSON string representation of the object
print DvsOperationBulkFaultFaultOnHost.to_json()

# convert the object into a dict
dvs_operation_bulk_fault_fault_on_host_dict = dvs_operation_bulk_fault_fault_on_host_instance.to_dict()
# create an instance of DvsOperationBulkFaultFaultOnHost from a dict
dvs_operation_bulk_fault_fault_on_host_form_dict = dvs_operation_bulk_fault_fault_on_host.from_dict(dvs_operation_bulk_fault_fault_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


