# HostFeatureVersionKeyEnum

Set of possible values for *HostFeatureVersionInfo.key*, which is a unique key that identifies a feature.  Possible values: - `faultTolerance`: VMware Fault Tolerance feature.      For pre-4.1 hosts, the   version value reported will be empty in which case   *AboutInfo.build* should be used. For all   other hosts, the version number reported will be a component-specific   version identifier of the form X.Y.Z, where:   X refers to host agent Fault Tolerance version number,   Y refers to VMX Fault Tolerance version number,   Z refers to VMkernal Fault Tolerance version  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


