# FaultsByVM

VM specific faults.  This Class is used in e.g. *HostEnterMaintenanceResult*.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**faults** | [**List[MethodFault]**](MethodFault.md) | The array of faults related to the given VM.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.faults_by_vm import FaultsByVM

# TODO update the JSON string below
json = "{}"
# create an instance of FaultsByVM from a JSON string
faults_by_vm_instance = FaultsByVM.from_json(json)
# print the JSON string representation of the object
print FaultsByVM.to_json()

# convert the object into a dict
faults_by_vm_dict = faults_by_vm_instance.to_dict()
# create an instance of FaultsByVM from a dict
faults_by_vm_form_dict = faults_by_vm.from_dict(faults_by_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


