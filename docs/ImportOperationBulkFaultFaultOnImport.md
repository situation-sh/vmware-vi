# ImportOperationBulkFaultFaultOnImport

The fault occurred on the entity during an import operation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity type on which import failed.  See *EntityType_enum* for valid values  ***Since:*** vSphere API 5.1  | [optional] 
**key** | **str** | The key on which import failed  ***Since:*** vSphere API 5.1  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.import_operation_bulk_fault_fault_on_import import ImportOperationBulkFaultFaultOnImport

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOperationBulkFaultFaultOnImport from a JSON string
import_operation_bulk_fault_fault_on_import_instance = ImportOperationBulkFaultFaultOnImport.from_json(json)
# print the JSON string representation of the object
print ImportOperationBulkFaultFaultOnImport.to_json()

# convert the object into a dict
import_operation_bulk_fault_fault_on_import_dict = import_operation_bulk_fault_fault_on_import_instance.to_dict()
# create an instance of ImportOperationBulkFaultFaultOnImport from a dict
import_operation_bulk_fault_fault_on_import_form_dict = import_operation_bulk_fault_fault_on_import.from_dict(import_operation_bulk_fault_fault_on_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


