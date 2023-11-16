# DvsOperationBulkFault

Thrown if a DistributedVirtualSwitch operation failed on some of the host members.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_fault** | [**List[DvsOperationBulkFaultFaultOnHost]**](DvsOperationBulkFaultFaultOnHost.md) | Faults occurred on the host during a DistributedVirtualSwitch operation.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_operation_bulk_fault import DvsOperationBulkFault

# TODO update the JSON string below
json = "{}"
# create an instance of DvsOperationBulkFault from a JSON string
dvs_operation_bulk_fault_instance = DvsOperationBulkFault.from_json(json)
# print the JSON string representation of the object
print DvsOperationBulkFault.to_json()

# convert the object into a dict
dvs_operation_bulk_fault_dict = dvs_operation_bulk_fault_instance.to_dict()
# create an instance of DvsOperationBulkFault from a dict
dvs_operation_bulk_fault_form_dict = dvs_operation_bulk_fault.from_dict(dvs_operation_bulk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


