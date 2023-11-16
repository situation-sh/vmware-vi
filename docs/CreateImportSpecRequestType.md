# CreateImportSpecRequestType

The parameters of *OvfManager.CreateImportSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_descriptor** | **str** | The OVF descriptor of the entity.  | 
**resource_pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**cisp** | [**OvfCreateImportSpecParams**](OvfCreateImportSpecParams.md) |  | 

## Example

```python
from vmware_vi.models.create_import_spec_request_type import CreateImportSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportSpecRequestType from a JSON string
create_import_spec_request_type_instance = CreateImportSpecRequestType.from_json(json)
# print the JSON string representation of the object
print CreateImportSpecRequestType.to_json()

# convert the object into a dict
create_import_spec_request_type_dict = create_import_spec_request_type_instance.to_dict()
# create an instance of CreateImportSpecRequestType from a dict
create_import_spec_request_type_form_dict = create_import_spec_request_type.from_dict(create_import_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


