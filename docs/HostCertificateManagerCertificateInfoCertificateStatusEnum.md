# HostCertificateManagerCertificateInfoCertificateStatusEnum

The status of a given certificate as computed per the soft and the hard thresholds in vCenter Server.        There are two different thresholds for the host certificate expirations; a soft threshold (which constitutes of two phases) and a hard threshold.       Soft Threshold:    Phase One: vCenter Server will publish an event at this time to let the user know about the status, but, no alarms or warnings are raised.    Phase Two: During this phase, vCenter Server will publish an event and indicate the certificate status as expiring in the UI.       Hard Threshold:    vCenter Server will publish an alarm and indicate via the UI that the certificate expiration is imminent.  Possible values: - `unknown`: The certificate status is unknown. - `expired`: The certificate has expired. - `expiring`: The certificate is expiring shortly.      (soft threshold - 1) - `expiringShortly`: The certificate is expiring shortly.      (soft threshold - 2) - `expirationImminent`: The certificate expiration is imminent.      (hard threshold) - `good`: The certificate is good.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


