# NotEnoughCpus

The host hardware does not have enough CPU cores to support the number of virtual CPUs in the virtual machine.  If the host is using hyperthreading, NotEnoughLogicalCpus is employed instead of NotEnoughCpus. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cpu_dest** | **int** | The number of CPUs present on the host.  | 
**num_cpu_vm** | **int** | The number of virtual CPUs present in the virtual machine.  | 

## Example

```python
from vmware_vi.models.not_enough_cpus import NotEnoughCpus

# TODO update the JSON string below
json = "{}"
# create an instance of NotEnoughCpus from a JSON string
not_enough_cpus_instance = NotEnoughCpus.from_json(json)
# print the JSON string representation of the object
print NotEnoughCpus.to_json()

# convert the object into a dict
not_enough_cpus_dict = not_enough_cpus_instance.to_dict()
# create an instance of NotEnoughCpus from a dict
not_enough_cpus_form_dict = not_enough_cpus.from_dict(not_enough_cpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


