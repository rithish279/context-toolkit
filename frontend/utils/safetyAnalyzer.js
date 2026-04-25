// Detect if critical information was forgotten
export const analyzeSafety = (fullConversation, keptMessages) => {
  const criticalKeywords = [
    'allergic', 'allergy', 'allergies',
    'can\'t eat', 'cannot eat',
    'deadly', 'fatal',
    'medical condition', 'diagnosis',
    'prescription', 'medication'
  ];
  
  const fullText = fullConversation.join(' ').toLowerCase();
  const keptText = keptMessages.join(' ').toLowerCase();
  
  const hasCriticalInfo = criticalKeywords.some(keyword => 
    fullText.includes(keyword)
  );
  
  if (!hasCriticalInfo) {
    return { isDangerous: false, warning: null };
  }
  
  const retainedCriticalInfo = criticalKeywords.some(keyword => 
    keptText.includes(keyword)
  );
  
  if (!retainedCriticalInfo) {
    return {
      isDangerous: true,
      warning: 'DANGER: Critical safety information was forgotten'
    };
  }
  
  return { isDangerous: false, warning: null };
};

export const calculateEfficiency = (tokensUsed, totalMessages, keptCount) => {
  const tokenEfficiency = ((totalMessages - keptCount) / totalMessages) * 100;
  return Math.round(tokenEfficiency);
};