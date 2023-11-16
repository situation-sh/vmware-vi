# TooManyDisksOnLegacyHost

Deprecated as of vSphere 4.1, this error condition is no longer possible.  The VM has too many disks which can cause the VM to take a long time to power-on.  This can result in migration taking a long time to complete or to fail due to timeout. This is a problem only for migration of powered-on virtual machines from or to ESX 2.x hosts.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_count** | **int** | The number disks this VM has.  ***Since:*** VI API 2.5  | 
**timeout_danger** | **bool** | Whether this number of disks will cause a timeout failure.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.too_many_disks_on_legacy_host import TooManyDisksOnLegacyHost

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyDisksOnLegacyHost from a JSON string
too_many_disks_on_legacy_host_instance = TooManyDisksOnLegacyHost.from_json(json)
# print the JSON string representation of the object
print TooManyDisksOnLegacyHost.to_json()

# convert the object into a dict
too_many_disks_on_legacy_host_dict = too_many_disks_on_legacy_host_instance.to_dict()
# create an instance of TooManyDisksOnLegacyHost from a dict
too_many_disks_on_legacy_host_form_dict = too_many_disks_on_legacy_host.from_dict(too_many_disks_on_legacy_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


