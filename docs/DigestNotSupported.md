# DigestNotSupported

The digest file of the specified virtual disk is not supported.  Typically, this fault is returned as part of a parent fault like *VmConfigIncompatibleForFaultTolerance*, indicating that the virtual disk's digest file needs to be changed before fault tolerance can be enabled on the associated virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.digest_not_supported import DigestNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DigestNotSupported from a JSON string
digest_not_supported_instance = DigestNotSupported.from_json(json)
# print the JSON string representation of the object
print DigestNotSupported.to_json()

# convert the object into a dict
digest_not_supported_dict = digest_not_supported_instance.to_dict()
# create an instance of DigestNotSupported from a dict
digest_not_supported_form_dict = digest_not_supported.from_dict(digest_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


