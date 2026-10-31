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
  An encrypted stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another obfuscated form in such a way that reversing the conversion to obtain the original data form can only be accomplished through possession and use of a specific key.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EncryptedStreamFacet extends Facet {

  private List<String> encryptionIV;
  private List<String> encryptionKey;
  private String encryptionMethod;
  private String encryptionMode;


}