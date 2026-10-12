import React from 'react';
import { AbsoluteFill, Img, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export type PromoProps = {
  title: string;
  subtitle: string;
  imageUrl: string;
  durationInFrames: number;
};

export const Promo: React.FC<PromoProps> = ({ title, subtitle, imageUrl }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const enter = spring({ frame, fps, config: { damping: 200 } });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const zoom = interpolate(frame, [0, durationInFrames], [1, 1.08]);
  return (
    <AbsoluteFill style={{ background: 'linear-gradient(160deg,#111827,#1f2937)', opacity: fadeOut, fontFamily: 'Helvetica, Arial, sans-serif' }}>
      {imageUrl ? (
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', top: 200, bottom: 700 }}>
          <Img src={imageUrl} style={{ maxWidth: 900, maxHeight: 900, objectFit: 'contain', transform: `scale(${zoom})`, borderRadius: 32 }} />
        </AbsoluteFill>
      ) : null}
      <AbsoluteFill style={{ justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 260, transform: `translateY(${(1 - enter) * 120}px)` }}>
        <div style={{ color: 'white', fontSize: 96, fontWeight: 800, textAlign: 'center', padding: '0 60px' }}>{title}</div>
        <div style={{ color: '#d1d5db', fontSize: 56, marginTop: 24, textAlign: 'center', padding: '0 60px' }}>{subtitle}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
