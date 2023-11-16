# PerformDvsProductSpecOperationRequestType

The parameters of *DistributedVirtualSwitch.PerformDvsProductSpecOperation_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation. See *DistributedVirtualSwitchProductSpecOperationType_enum* for valid values. For *VmwareDistributedVirtualSwitch*, only *upgrade* is valid.  | 
**product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.perform_dvs_product_spec_operation_request_type import PerformDvsProductSpecOperationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PerformDvsProductSpecOperationRequestType from a JSON string
perform_dvs_product_spec_operation_request_type_instance = PerformDvsProductSpecOperationRequestType.from_json(json)
# print the JSON string representation of the object
print PerformDvsProductSpecOperationRequestType.to_json()

# convert the object into a dict
perform_dvs_product_spec_operation_request_type_dict = perform_dvs_product_spec_operation_request_type_instance.to_dict()
# create an instance of PerformDvsProductSpecOperationRequestType from a dict
perform_dvs_product_spec_operation_request_type_form_dict = perform_dvs_product_spec_operation_request_type.from_dict(perform_dvs_product_spec_operation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


