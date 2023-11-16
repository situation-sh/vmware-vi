# DvsApplyOperationFault

Thrown if a vSphere Distributed Switch apply operation failed to set or remove some of the specified objects.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_fault** | [**List[DvsApplyOperationFaultFaultOnObject]**](DvsApplyOperationFaultFaultOnObject.md) | Faults occurred on the host during a DistributedVirtualSwitch operation.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_apply_operation_fault import DvsApplyOperationFault

# TODO update the JSON string below
json = "{}"
# create an instance of DvsApplyOperationFault from a JSON string
dvs_apply_operation_fault_instance = DvsApplyOperationFault.from_json(json)
# print the JSON string representation of the object
print DvsApplyOperationFault.to_json()

# convert the object into a dict
dvs_apply_operation_fault_dict = dvs_apply_operation_fault_instance.to_dict()
# create an instance of DvsApplyOperationFault from a dict
dvs_apply_operation_fault_form_dict = dvs_apply_operation_fault.from_dict(dvs_apply_operation_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


