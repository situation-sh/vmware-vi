# FaultsByHost

Group of faults associated with Host.  This Class is used in e.g. *HostEnterMaintenanceResult*.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**faults** | [**List[MethodFault]**](MethodFault.md) | The array of faults related to the given Host.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.faults_by_host import FaultsByHost

# TODO update the JSON string below
json = "{}"
# create an instance of FaultsByHost from a JSON string
faults_by_host_instance = FaultsByHost.from_json(json)
# print the JSON string representation of the object
print FaultsByHost.to_json()

# convert the object into a dict
faults_by_host_dict = faults_by_host_instance.to_dict()
# create an instance of FaultsByHost from a dict
faults_by_host_form_dict = faults_by_host.from_dict(faults_by_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


