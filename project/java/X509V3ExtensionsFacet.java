package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An X.509 v3 certificate extensions facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class X509V3ExtensionsFacet extends Facet {

  private String authorityKeyIdentifier;
  private String basicConstraints;
  private String certificatePolicies;
  private String crlDistributionPoints;
  private String extendedKeyUsage;
  private String inhibitAnyPolicy;
  private String issuerAlternativeName;
  private String keyUsage;
  private String nameConstraints;
  private String policyConstraints;
  private String policyMappings;
  private ZonedDateTime privateKeyUsagePeriodNotAfter;
  private ZonedDateTime privateKeyUsagePeriodNotBefore;
  private String subjectAlternativeName;
  private String subjectDirectoryAttributes;
  private String subjectKeyIdentifier;


}