# ImportVAppRequestType

The parameters of *ResourcePool.ImportVApp*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**ImportSpec**](ImportSpec.md) |  | 
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.import_v_app_request_type import ImportVAppRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ImportVAppRequestType from a JSON string
import_v_app_request_type_instance = ImportVAppRequestType.from_json(json)
# print the JSON string representation of the object
print ImportVAppRequestType.to_json()

# convert the object into a dict
import_v_app_request_type_dict = import_v_app_request_type_instance.to_dict()
# create an instance of ImportVAppRequestType from a dict
import_v_app_request_type_form_dict = import_v_app_request_type.from_dict(import_v_app_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


