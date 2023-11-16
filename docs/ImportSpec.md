# ImportSpec

An ImportSpec is used when importing VMs or vApps.  It can be built from scratch, or it can be generated from an OVF descriptor using the service interface *OvfManager*.  This class is the abstract base for *VirtualMachineImportSpec* and *VirtualAppImportSpec*. These three classes form a composite structure that allows us to contain arbitrarily complex entitites in a single ImportSpec.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_config** | [**VAppEntityConfigInfo**](VAppEntityConfigInfo.md) |  | [optional] 
**instantiation_ost** | [**OvfConsumerOstNode**](OvfConsumerOstNode.md) |  | [optional] 

## Example

```python
from vmware_vi.models.import_spec import ImportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSpec from a JSON string
import_spec_instance = ImportSpec.from_json(json)
# print the JSON string representation of the object
print ImportSpec.to_json()

# convert the object into a dict
import_spec_dict = import_spec_instance.to_dict()
# create an instance of ImportSpec from a dict
import_spec_form_dict = import_spec.from_dict(import_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


