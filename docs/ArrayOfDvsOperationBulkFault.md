# ArrayOfDvsOperationBulkFault

A boxed array of *DvsOperationBulkFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsOperationBulkFault]**](DvsOperationBulkFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_operation_bulk_fault import ArrayOfDvsOperationBulkFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsOperationBulkFault from a JSON string
array_of_dvs_operation_bulk_fault_instance = ArrayOfDvsOperationBulkFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsOperationBulkFault.to_json()

# convert the object into a dict
array_of_dvs_operation_bulk_fault_dict = array_of_dvs_operation_bulk_fault_instance.to_dict()
# create an instance of ArrayOfDvsOperationBulkFault from a dict
array_of_dvs_operation_bulk_fault_form_dict = array_of_dvs_operation_bulk_fault.from_dict(array_of_dvs_operation_bulk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


