# NumVirtualCpusExceedsLimit

This fault is thrown when the total number of virtual CPUs present or requested in virtual machines' configuration has exceeded the limit on the host.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_supported_vcpus** | **int** | The maximum number of virtual CPUs supported on the host.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.num_virtual_cpus_exceeds_limit import NumVirtualCpusExceedsLimit

# TODO update the JSON string below
json = "{}"
# create an instance of NumVirtualCpusExceedsLimit from a JSON string
num_virtual_cpus_exceeds_limit_instance = NumVirtualCpusExceedsLimit.from_json(json)
# print the JSON string representation of the object
print NumVirtualCpusExceedsLimit.to_json()

# convert the object into a dict
num_virtual_cpus_exceeds_limit_dict = num_virtual_cpus_exceeds_limit_instance.to_dict()
# create an instance of NumVirtualCpusExceedsLimit from a dict
num_virtual_cpus_exceeds_limit_form_dict = num_virtual_cpus_exceeds_limit.from_dict(num_virtual_cpus_exceeds_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


