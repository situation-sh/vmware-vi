# ArrayOfFaultsByHost

A boxed array of *FaultsByHost*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultsByHost]**](FaultsByHost.md) |  | 

## Example

```python
from vmware_vi.models.array_of_faults_by_host import ArrayOfFaultsByHost

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultsByHost from a JSON string
array_of_faults_by_host_instance = ArrayOfFaultsByHost.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultsByHost.to_json()

# convert the object into a dict
array_of_faults_by_host_dict = array_of_faults_by_host_instance.to_dict()
# create an instance of ArrayOfFaultsByHost from a dict
array_of_faults_by_host_form_dict = array_of_faults_by_host.from_dict(array_of_faults_by_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


