# ImportOperationBulkFault

Thrown if a Import operation fails  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_faults** | [**List[ImportOperationBulkFaultFaultOnImport]**](ImportOperationBulkFaultFaultOnImport.md) | Faults occurred during the import operation  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.import_operation_bulk_fault import ImportOperationBulkFault

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOperationBulkFault from a JSON string
import_operation_bulk_fault_instance = ImportOperationBulkFault.from_json(json)
# print the JSON string representation of the object
print ImportOperationBulkFault.to_json()

# convert the object into a dict
import_operation_bulk_fault_dict = import_operation_bulk_fault_instance.to_dict()
# create an instance of ImportOperationBulkFault from a dict
import_operation_bulk_fault_form_dict = import_operation_bulk_fault.from_dict(import_operation_bulk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


