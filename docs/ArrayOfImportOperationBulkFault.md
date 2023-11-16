# ArrayOfImportOperationBulkFault

A boxed array of *ImportOperationBulkFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ImportOperationBulkFault]**](ImportOperationBulkFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_import_operation_bulk_fault import ArrayOfImportOperationBulkFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfImportOperationBulkFault from a JSON string
array_of_import_operation_bulk_fault_instance = ArrayOfImportOperationBulkFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfImportOperationBulkFault.to_json()

# convert the object into a dict
array_of_import_operation_bulk_fault_dict = array_of_import_operation_bulk_fault_instance.to_dict()
# create an instance of ArrayOfImportOperationBulkFault from a dict
array_of_import_operation_bulk_fault_form_dict = array_of_import_operation_bulk_fault.from_dict(array_of_import_operation_bulk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


