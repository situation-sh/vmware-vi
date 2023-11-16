# DvsApplyOperationFaultFaultOnObject

The fault occurred during an apply operation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | The object identifier.  It should be UUID for vSphere Distributed Switches, keys for vNetwork distributed portgroups and ports.  ***Since:*** vSphere API 5.1  | 
**type** | **str** | The Type of the objects.  ***Since:*** vSphere API 5.1  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.dvs_apply_operation_fault_fault_on_object import DvsApplyOperationFaultFaultOnObject

# TODO update the JSON string below
json = "{}"
# create an instance of DvsApplyOperationFaultFaultOnObject from a JSON string
dvs_apply_operation_fault_fault_on_object_instance = DvsApplyOperationFaultFaultOnObject.from_json(json)
# print the JSON string representation of the object
print DvsApplyOperationFaultFaultOnObject.to_json()

# convert the object into a dict
dvs_apply_operation_fault_fault_on_object_dict = dvs_apply_operation_fault_fault_on_object_instance.to_dict()
# create an instance of DvsApplyOperationFaultFaultOnObject from a dict
dvs_apply_operation_fault_fault_on_object_form_dict = dvs_apply_operation_fault_fault_on_object.from_dict(dvs_apply_operation_fault_fault_on_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


