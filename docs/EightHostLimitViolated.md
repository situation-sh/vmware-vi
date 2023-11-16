# EightHostLimitViolated

Only virtual machines on eight different hosts can have a single virtual disk backing opened for read at once.  This fault occurs when moving or powering on this virtual machine would cause a violation of the above constraint. This only occurs when multiple virtual machines are sharing a single disk backing.  Note that there is no limit on the number of virtual machines who share a disk backings, so long as they are running on eight or fewer hosts.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.eight_host_limit_violated import EightHostLimitViolated

# TODO update the JSON string below
json = "{}"
# create an instance of EightHostLimitViolated from a JSON string
eight_host_limit_violated_instance = EightHostLimitViolated.from_json(json)
# print the JSON string representation of the object
print EightHostLimitViolated.to_json()

# convert the object into a dict
eight_host_limit_violated_dict = eight_host_limit_violated_instance.to_dict()
# create an instance of EightHostLimitViolated from a dict
eight_host_limit_violated_form_dict = eight_host_limit_violated.from_dict(eight_host_limit_violated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


