# HostMultipathInfoLogicalUnitPolicy

The *HostMultipathInfoLogicalUnitPolicy* data object describes a path selection policy for a device.  This policy determines how paths should be utilized when accessing a device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | String representing the path selection policy for a device.  Use one of the following strings: For NMP plugin - &lt;code&gt;VMW\\_PSP\\_FIXED&lt;/code&gt; - Use a preferred path whenever possible. - &lt;code&gt;VMW\\_PSP\\_RR&lt;/code&gt; - Load balance. - &lt;code&gt;VMW\\_PSP\\_MRU&lt;/code&gt; - Use the most recently used path.    For HPP plugin - &lt;code&gt;FIXED&lt;/code&gt; - Use a preferred path whenever possible. - &lt;code&gt;LB-RR&lt;/code&gt; - Load Balance - round robin. - &lt;code&gt;LB-IOPS&lt;/code&gt; - Load Balance - iops. - &lt;code&gt;LB-BYTES&lt;/code&gt; - Load Balance - bytes. - &lt;code&gt;LB--Latency&lt;/code&gt; - Load balance - least latency.    You can also use the *HostStorageSystem.QueryPathSelectionPolicyOptions* method to retrieve the set of valid strings. Use the key from the resulting structure *HostPathSelectionPolicyOption*.  | 

## Example

```python
from vmware_vi.models.host_multipath_info_logical_unit_policy import HostMultipathInfoLogicalUnitPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoLogicalUnitPolicy from a JSON string
host_multipath_info_logical_unit_policy_instance = HostMultipathInfoLogicalUnitPolicy.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoLogicalUnitPolicy.to_json()

# convert the object into a dict
host_multipath_info_logical_unit_policy_dict = host_multipath_info_logical_unit_policy_instance.to_dict()
# create an instance of HostMultipathInfoLogicalUnitPolicy from a dict
host_multipath_info_logical_unit_policy_form_dict = host_multipath_info_logical_unit_policy.from_dict(host_multipath_info_logical_unit_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


