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
  A X.509 certificate facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 PKI (Public Key Infrastructure) standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class X509CertificateFacet extends Facet {

  private Boolean isSelfSigned;
  private String issuer;
  private Hash issuerHash;
  private String observableVersion;
  private String serialNumber;
  private String signature;
  private String signatureAlgorithm;
  private String subject;
  private Hash subjectHash;
  private String subjectPublicKeyAlgorithm;
  private Integer subjectPublicKeyExponent;
  private String subjectPublicKeyModulus;
  private Hash thumbprintHash;
  private ZonedDateTime validityNotAfter;
  private ZonedDateTime validityNotBefore;
  private X509V3ExtensionsFacet x509v3extensions;


}